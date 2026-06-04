# Assumptions

1. Each component belongs to one category (Frame, Gear, Tyre, Brake, Seat).
2. A component can have multiple price records.
3. Prices are effective from a specific date.
4. The latest price before or on the selected pricing date is considered valid.
5. All selected components must exist in the database.
6. Historical prices are never modified or deleted.
7. The pricing engine calculates the total bicycle cost using component-level prices.
8. Salespersons can save configurations for future reference.
9. Only one component per category can be selected while building a bicycle.
10. The system is designed for demonstration purposes and does not include authentication.
