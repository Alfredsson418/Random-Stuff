#include <iostream>
#include "fun.hpp"



int main() {
    std::string motherboard, cpu, gpu, psu, ram;
    bool done;

    std::cout << "Motherboard: ";
    std::getline(std::cin, motherboard);

    std::cout << "CPU: ";
    std::getline(std::cin, cpu);

    std::cout << "PSU: ";
    std::getline(std::cin, psu);

    std::cout << "Ram: ";
    std::getline(std::cin, ram);


    PC dator(motherboard, cpu, psu, ram);

    dator.new_gpu("RTX 2060 6GB");

    save_PC(dator.get_PC());

    std::cout << "done?";
    std::cin >> done;
}
