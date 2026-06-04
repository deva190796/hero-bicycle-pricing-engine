from backend.crud import get_price_for_date

def calculate_bicycle_price(db, request):

    breakdown = []
    total = 0

    components = {
        "Frame": request.frame_id,
        "Gear": request.gear_id,
        "Tyre": request.tyre_id,
        "Brake": request.brake_id,
        "Seat": request.seat_id
    }

    for name, component_id in components.items():

        price_record = get_price_for_date(
            db,
            component_id,
            request.pricing_date
        )

        if price_record:
            breakdown.append({
                "component": name,
                "price": price_record.price
            })

            total += price_record.price

    return {
        "pricing_date": request.pricing_date,
        "total_price": total,
        "breakdown": breakdown
    }