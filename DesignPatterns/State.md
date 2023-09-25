# State

> Fun with Finite State Machines.
>

<aside>
💡 A pattern in which the object’s behavior is determined by its state. An object transitions from one state to another (something needs to trigger a transition).

</aside>

<aside>
💡 A formalized construct which manages state and transitions is called a state machine.

</aside>

## Intent:

### Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Explanation:

> The State pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. Instead of implementing a state-dependent behavior within a class, the State pattern suggests creating new classes for all states and extracting all state-specific behavior into these classes. The original object, called context, keeps a reference to a state object that represents its current state, and delegates all the state-related work to this object.
>

---

### Motivation to use:

- Consider an ordinary telephone
- What you do with it depends on the state of the phone/line
    - If it’s ringing or you want to make a call, you can pick it up
    - Phone must be off the hook to talk/make a call
    - If you try calling someone, and it’s busy, you put the handset down
- Changes in state can be explicit or in response to event (Observer pattern)

---

## Summary from the course:

- Given sufficient complexity, it pays to formally define possible states and events/triggers
- Can define
    - State entry/exit behaviors
    - Action when a particular event causes a transition
    - Guard conditions enabling/disabling a transition
    - Default action when no transitions are found for an event

---