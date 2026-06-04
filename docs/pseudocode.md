# Pseudocode

START

Load all bicycle components

User selects:

* Frame
* Gear Set
* Tyre
* Brake
* Seat
* Pricing Date

FOR each selected component

```
Find latest price record
WHERE effective_from <= pricing_date

Add component price to total

Add component price to breakdown
```

END FOR

Display:

* Component-wise breakdown
* Total Bicycle Price

IF user clicks Save Configuration

```
Store selected components
Store total price
```

END IF

END
