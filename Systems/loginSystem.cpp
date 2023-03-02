#include <iostream>
#include <fstream>
#include <string>


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

int main() {
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
        } else {
            std::cout << "Invalid Login Details\n";
        }
    }

        break;
    
    case 2:
        Register(username, password);
        break;

    default:
        std::cout << "Invalid choice responce";

    }



}