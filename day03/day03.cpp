#include <iostream>
#include <fstream>
#include <string>
#include <set>

int main() {
    std::string line;
    std::ifstream inp ("input.txt");

    std::set<std::string> houses;
    std::set<std::string> robo_houses;

    int x = 0;
    int y = 0;
    int sx = 0;
    int sy = 0;
    int rx = 0;
    int ry = 0;

    std::string pos;
    std::string spos;
    std::string rpos;

    bool robo = false;

    if (inp.is_open()) {
        while (getline(inp, line)) {
            for (int i = 0; i < line.length(); i++) {
                char c = line[i];

                switch (c) {
                    case '>': x++; robo ? rx++ : sx++; break;
                    case '<': x--; robo ? rx-- : sx--; break;
                    case '^': y++; robo ? ry++ : sy++; break;
                    case 'v': y--; robo ? ry-- : sy--; break;
                }

                pos = std::to_string(x) + "," + std::to_string(y);
                houses.insert(pos);

                if (robo) {
                    rpos = std::to_string(rx) + "," + std::to_string(ry);
                    robo_houses.insert(rpos);
                } else {
                    spos = std::to_string(sx) + "," + std::to_string(sy);
                    robo_houses.insert(spos);
                }

                robo = !robo;
            }
        }

        std::cout << "Santa Only: " << houses.size() << '\n';
        std::cout << "Robo Santa: " << robo_houses.size() << '\n';
    }
    else std::cout << "Unable to open input.txt";

    return 0;
}
