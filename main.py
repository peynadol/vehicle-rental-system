import vehicle_data


def main():
    vehicle = vehicle_data.vehicle_data["C001"]

    vehicle.check_out()

    vehicle.return_vehicle()


if __name__ == '__main__':
    main()
