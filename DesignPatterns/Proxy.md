# Proxy

> An interface for accessing a particular resource.
>

<aside>
💡 A class that functions as an interface to a particular resource. That resource may be remote, expensive to construct, or may require logging or some other added functionality.

</aside>

## Intent:

### Provide a surrogate or placeholder for another object to control access to it.

## Explanation:

> The Proxy pattern provides a surrogate or placeholder for another object to control access to it. It usually involves creating an interface that both the RealObject and Proxy classes implement. The Proxy class can manage the creation of the RealObject and the RealObject's interaction with the client, providing additional functionality like caching, lazy initialization, or access control.
>

---

### Motivation to use:

- You are calling foo.Bar()
- This assumes that foo is in the same process as Bar()
- What if, later on, you want to put all Foo-related operations into a separate process
    - Can you avoid changing your code?
- Proxy to the rescue!
    - Same interface, entirely different behavior
- This is called a communication proxy
    - Other types: logging, virtual, guarding, …

---

## Summary from the course:

- A proxy has the same interface as the underlying object
- To create a proxy, simply replicate the existing interface of an object
- Add relevant functionality to the redefined member functions
- Different proxies (communication, logging, caching, etc.) have completely different behaviors

---