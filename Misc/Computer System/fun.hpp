#include <string>

class PC {

std::string cpu = "None";

std::string gpu = "None";
int gpu_vram = 0;

std::string psu = "None";

std::string ram = "None";

std::string motherboard = "None";

std::string PC_save = "None";

std::string personal_pc;

public:

    PC(std::string new_motherboard, std::string new_cpu, std::string new_psu, std::string new_ram);

    void new_cpu(std::string new_cpu);

    void new_gpu(std::string new_gpu);

    void new_psu(std::string new_psu);

    void new_ram(std::string new_ram);

    void new_motherboard(std::string new_motherboard);

    

    std::string get_PC();

};

void save_PC(std::string PC_save);