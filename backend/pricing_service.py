from backend.crud import get_latest_price

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

        latest_price = get_latest_price(db, component_id)

        if latest_price:
            breakdown.append({
                "component": name,
                "price": latest_price.price
            })

            total += latest_price.price

    return {
        "total_price": total,
        "breakdown": breakdown
    }