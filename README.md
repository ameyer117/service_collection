Here's the updated README with an example including the creation and usage of the `inject` function:

---

# service_collection

`service_collection` is a lightweight Python package that mimics ASP.NET's dependency injection system. It also incorporates an Angular-style `Inject` method to resolve dependencies, making it easier to manage and inject dependencies in your applications.
It currently supports transient and singleton services. Scoped services will be added in a future release if there is a demand for them.

## Installation

Install the package using pip:

```bash
pip install service_collection
```

## Usage

### Setting Up the Service Collection

1. **Define your services and interfaces**:

```python
from abc import ABC, abstractmethod

# Define an abstract base class for the service interface
class IFooService(ABC):
    @abstractmethod
    def do_something(self):
        pass

# Implement the interface
class FooService(IFooService):
    def do_something(self):
        return "FooService did something!"

# Define another service that depends on the interface
class IBarService(ABC):
    @abstractmethod
    def do_something(self):
        pass

class BarService(IBarService):
    def __init__(self, foo_service: IFooService):
        self.foo_service = foo_service

    def do_something(self):
        return f"BarService did something with {self.foo_service.do_something()}"
```

2. **Register your services**:

```python
from service_collection import ServiceCollection

services = ServiceCollection()
services.add_transient(IFooService, FooService)
services.add_singleton(IBarService, BarService)
```

3. **Build the service provider**:

```python
service_provider = services.build_service_provider()
```

### Creating and Using the Inject Function

Define an `inject` function to retrieve service instances easily in your code:

```python
def inject(service_type):
    return service_provider.get_service(service_type)
```

Use the `inject` function to resolve services:

```python
foo_service = inject(IFooService)
print(foo_service.do_something())  # Output: FooService did something!

bar_service = inject(IBarService)
print(bar_service.do_something())  # Output: BarService did something with FooService did something!
```

### Full Example

Here is a complete example demonstrating how to set up and use the `service_collection` package with the `inject` function:

```python
from abc import ABC, abstractmethod
from service_collection import ServiceCollection

# Define an abstract base class for the service interface
class IFooService(ABC):
    @abstractmethod
    def do_something(self):
        pass

# Implement the interface
class FooService(IFooService):
    def do_something(self):
        return "FooService did something!"

# Define another service that depends on the interface
class IBarService(ABC):
    @abstractmethod
    def do_something(self):
        pass

class BarService(IBarService):
    def __init__(self, foo_service: IFooService):
        self.foo_service = foo_service

    def do_something(self):
        return f"BarService did something with {self.foo_service.do_something()}"

# Register services
services = ServiceCollection()
services.add_transient(IFooService, FooService)
services.add_singleton(IBarService, BarService)

# Build the service provider
service_provider = services.build_service_provider()

# Define the inject function
def inject(service_type):
    return service_provider.get_service(service_type)

# Resolve and use services
foo_service = inject(IFooService)
print(foo_service.do_something())  # Output: FooService did something!

bar_service = inject(IBarService)
print(bar_service.do_something())  # Output: BarService did something with FooService did something!
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides an overview of how to install, set up, and use the `service_collection` package with example code snippets, demonstrating the use of abstract base classes for service interfaces and including the creation and usage of the `inject` function.