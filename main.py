import vehicle_data


def main():
    vehicle = vehicle_data.vehicle_data["C001"]
    vehicle.check_out()

    print(f"Availablity of {vehicle.model} is {vehicle.availablity}")


if __name__ == '__main__':
    main()
