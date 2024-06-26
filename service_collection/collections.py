from typing import Type, TypeVar, Dict, Any, Optional

TRANSIENT = "transient"
SINGLETON = "singleton"
INSTANCE = "instance"
IMPLEMENTATION = "implementation"
TYPE = "type"

T = TypeVar("T")
U = TypeVar("U")


class ServiceProvider:
    """
    Provides access to registered services and manages their lifetimes, including singleton and transient services.

    Attributes:
        _services (Dict[Type, Dict[str, Any]]): A dictionary storing the registered services and their metadata.
        _scoped_instances (Dict[str, Dict[Type[Any], Any]]): A dictionary storing scoped service instances.
    """

    def __init__(self, services: Dict[Type, Dict[str, Any]]):
        """
        Initializes a new instance of the ServiceProvider class.

        Args:
            services (Dict[Type, Dict[str, Any]]): The dictionary of registered services and their metadata.
        """
        self._services = services
        self._scoped_instances: Dict[str, Dict[Type[Any], Any]] = {}

    def get_service(self, service_type: Type[T]) -> T:
        """
        Retrieves an instance of the specified service type. Handles singleton and transient services.

        Args:
            service_type (Type[T]): The type of the service to retrieve.
        Returns:
            T: A concrete instance of the requested service type.

        Raises:
            Exception: If the requested service type is not registered.
        """

        service = self._services.get(service_type)
        if not service:
            raise Exception(f"Service {service_type} not registered.")

        if service[TYPE] == SINGLETON:
            if service[INSTANCE] is None:
                service[INSTANCE] = service[IMPLEMENTATION]()
            return service[INSTANCE]

        return service[IMPLEMENTATION]()


class ServiceCollection:
    """
    A collection of services for dependency injection, providing methods to add transient and singleton services.

    Attributes:
        _services (Dict[Type, Dict[str, Any]]): A dictionary storing the registered services and their metadata.
    """

    def __init__(self):
        self._services = {}

    def add_transient(self, interface_type: Type[T], implementation_type: Optional[Type[U]]):
        """
        Adds a transient service to the collection. Transient services are created each time they are requested.

        Args:
            interface_type (Type[T]): The interface or abstract class type of the service. (Contract type)
            implementation_type (Type[U]): The concrete implementation type of the service.

        Raises:
            ValueError: If either interface_type or implementation_type is not provided.
        """
        if not interface_type or not implementation_type:
            raise ValueError("Both interface_type and implementation_type must be provided")

        self._services[interface_type] = {
            TYPE: TRANSIENT,
            IMPLEMENTATION: implementation_type,
        }

    def add_singleton(self, interface_type: Type[T], implementation_type: Optional[Type[U]]):
        """
        Adds a singleton service to the collection. Singleton services are created once and shared across all requests.

        Args:
            interface_type (Type[T]): The interface or abstract class type of the service. (Contract type)
            implementation_type (Type[U]): The concrete implementation type of the service.

        Raises:
            ValueError: If both interface_type and implementation_type are not provided.
        """
        if not interface_type or not implementation_type:
            raise ValueError("Both interface_type and implementation_type must be provided")

        self._services[interface_type] = {
            TYPE: SINGLETON,
            IMPLEMENTATION: implementation_type,
            INSTANCE: None,
        }

    def build_service_provider(self):
        """
        Builds and returns a ServiceProvider instance from the registered services.

        Returns:
            ServiceProvider: An instance of ServiceProvider initialized with the registered services.
        """
        return ServiceProvider(self._services)


# Create a method like this to retrieve services easily in your code.
# def inject(service_type: Type[T]) -> T:
#     """
#     Retrieves an instance of the specified service type using the provided service provider.
#     Handles singleton, transient, and scoped services.
#
#     Args:
#         service_type (Type[T]): The type of the service to retrieve.
#
#     Returns:
#         T: An instance of the requested service type.
#
#     Raises:
#         Exception: If the requested service type is not registered or scope_id is required for scoped services.
#     """
#     return provider.get_service(service_type)
