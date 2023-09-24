# Design Patterns in Python

Design Patterns are reusable and customizable solutions to recurring problems in software development.
Overall, a design pattern is made up of four elements:

- **Pattern name**: the reference used to describe a design problem, its solutions and its consequences;
- **Problem**: the context in which design pattern is applicable;
- **Solution**: the elementary composition of the design pattern, its relationships, its responsibilities etc.
- **Consequences**: the advantages and disadvantages of applying the design pattern.

Nowadays, there are 23 design patterns distributed categorically in:

- **Creative Patterns**  

  Creation Design Patterns abstract the creative process. They help make a system independent of how its objects are created, composed and represented. 
  Currently, the design patterns in this category are:
  - **Abstract Factory** 

    Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

  - **Builder**

    Separates the complex object's construction from its representation so that the same construction process can create different representations.

  - **Factory Method**:

    Define uma interface para criar um objeto, mas permite que as subclasses decidam quais classes devem ser instanciadas.

  - **Prototype**:

    Specifies the objects's types to create using a prototype instance and create new objects by copying this prototype.

  - **Singleton**: 

    Ensures a class has only one instance by providing a global access point for it.
  
- **Structural Patterns**  

  Structural Design Patterns are concerned with way both classes and objects are composed to build larger structures.

  - **Adapter**
    
    Converts the class' interface to another interface expected by clients. The adapter allows certain classes to work together that would otherwise be impossible because of their incompatible interfaces.

  - **Bridge**
    
    Provides a proxy object for another object to control access to it.
    
  - **Façade**
    
    Provides a unified interface to a set of interfaces in a subsystem. The Façade defines a higher-level interface that makes the subsystem easier to use.

- **Behavioral Patterns**:

  Bahavioral Design Patterns are concerned with algorithms and assignment of responsibilities between objects. Behavioral patterns don't only describe of objects or    n classes, but also the patterns of communication between them.

  - **Observer**

    It is a behavioral design pattern that allows you to define a subscription mechanism to notify multiple objects about any events occurring on the object they are observing.

  - **Command**

    It is a behavioral design pattern that transforms a request into an independent object that contains all the information about the request. This transformation allows you to parameterize methods with different requests, delay or queue the execution of a request, and support undoable operations.
