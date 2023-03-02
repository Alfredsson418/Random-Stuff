#include <iostream>
#include <string>
#include <fstream>
#include <vector>


/*

Login System (You need to be logged in too use the Rental System)

Separate Menus for Admins and other users

Methods to calculate fares based on time and distance

Displaying car details, availability, etc


*/

class Car {
    private:
        double cost;
        const int seats;
        const std::string color;
        bool available;
        const int id;
    public:

        Car(double fare_cost, std::string car_color, int num_seats, bool availability, int car_id)
            : color(car_color), seats(num_seats), id(car_id) {

                cost = fare_cost;

                available = availability;

            }

        void DisplayCarDetails(bool show_availability = false) {
            std::cout << "---------------\n";
            std::cout << "Car ID: " << id << "\n";
            std::cout << "Color: " << color << "\n";
            std::cout << "Fare cost: " << cost << " per KM\n";
            std::cout << "Numer of Seats: " << seats << "\n";

            if (show_availability) {
                if (available) {
                    std::cout << "Available: Yes\n";
                } else {
                    std::cout << "Available: No\n";
                }

            }

        }



        double GetFareCost() {
            return cost;
        }

        double CalculateCost(double distance) {
            return cost * distance;
        }

        bool GetAvailability() {
            return available;
        }

        int GetID() {
            return id;
        }
  
};

void Register(std::string username, std::string password) {

    std::ofstream file ("data\\" + username + ".txt");

    file << username << "\n" << password;

    file.close();

}

bool Login(std::string username, std::string password) {

    std::string file_username, file_password;

    std::ifstream file ("data\\" + username + ".txt");
    std::getline(file, file_username);
    std::getline(file, file_password);

    if (file_username == username && file_password == password) {
        return true;
    }

    return false;

}

bool LoginProcess() {
    int choice;

    std::string username, password;

    std::cout << "1. Login\n";
    std::cout << "2. Register\n";

    std::cin >> choice;

    std::cout << "Username: "; std::cin >> username;
    std::cout << "Password: "; std::cin >> password;

    switch (choice) {
    case 1: 
    {
        bool status = Login(username, password);

        if (status) {
            std::cout << "Valid Login Details\n";
            return false;
        } else {
            std::cout << "Invalid Login Details\n";
            return true;
        }
    }

        break;
    
    case 2:
        Register(username, password);
        break;

    default:
        std::cout << "Invalid choice \n";

    }

    return true;
}


void ListAllCars(std::vector<Car> cars, bool show_availability = true, bool show_only_availability = false) {
    if (show_only_availability) {
        for (Car car : cars) {
            if (car.GetAvailability()){
                car.DisplayCarDetails(show_availability);
            }
        }
    } else {
        for (Car car : cars) {

            car.DisplayCarDetails(show_availability);

        }
    }

}

bool IfIdExist(std::vector<Car> cars, int id) {

    for (Car car : cars) {
        if (car.GetID() == id) {
            return true;
        }
    }

    return false;


}


int main() {
    bool run = true;
    while (run) {
        run = LoginProcess();
    }

    /* Loads cars with vector*/

    std::vector<Car> cars = {
        Car(36.0, "Red", 4, true, 1),
        Car(36.6, "Blue", 2, true, 2),
        Car(26.0, "Yellow", 2, false, 3)
    };



    std::cout << "Welcome \n";


    while (true) {

        int choice;
        std::cout << "---------------\n";
        std::cout << "1. List all cars\n";
        std::cout << "2. List all AVALIBLE cars\n";
        std::cout << "3. Calculate route\n";
        std::cout << "4. Exit\n";

        std::cin >> choice;


        switch (choice) {
        case 1:
            ListAllCars(cars);
            break;
        
        case 2:
            ListAllCars(cars, false, true);
            break;

        case 3:
        {
            int km;
            std::cout << "How far (in KM) do you want to go? \n";
            std::cin >> km;
            for (Car car : cars) {
                std::cout << "------------\n";
                std::cout << "Car ID: " << car.GetID() << "\n";
                std::cout << "Cost: " << car.CalculateCost(km) << "kr\n";
            }
        }
            break;
        default:
            break;
        } 

        if (choice == 4) {
            std::cout << "Bye!\n";
            break;
        }

    }




}