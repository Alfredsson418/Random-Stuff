#include "fun.hpp"
#include <iostream>
#include <fstream>
using namespace std;

//Creates a basic PC
PC::PC(std::string new_motherboard, std::string new_cpu, std::string new_psu, std::string new_ram) {

    motherboard = new_motherboard;

    cpu = new_cpu;

    psu = new_psu;

    ram = new_ram;

}

//Returns PC as string
std::string PC::get_PC() {

    std::string components = "";
    components += "CPU: " + cpu + "\n";
    components += "Motherboard: " + motherboard + "\n";
    components += "GPU: " + gpu + "\n";
    components += "PSU: " + psu + "\n";
    components += "RAM: " + ram + "\n";

    return components;

}

//Changes or create new components
void PC::new_cpu(std::string new_cpu) {
    cpu = new_cpu;
}

void PC::new_gpu(std::string new_gpu) {
    gpu = new_gpu;
}

void PC::new_psu(std::string new_psu) {
    psu = new_psu;
}

void PC::new_ram(std::string new_ram) {
    ram = new_ram;
}

void PC::new_motherboard(std::string new_motherboard) {
    motherboard = new_motherboard;
}

// Saves PC as a file
void save_PC(std::string PC_save) {
    ofstream MyFile("text filer\\dator.txt");

    MyFile << PC_save << "\n";

    MyFile.close();
}

