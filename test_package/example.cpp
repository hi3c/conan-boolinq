#include <iostream>
#include <boolinq/boolinq.h>

using namespace boolinq;

int main() {
  int src[] = {1,2,3,4,5,6,7,8};
  auto dst = from(src).where( [](int a){return a%2 == 1;})    // 1,3,5,7
                      .select([](int a){return a*2;})         // 2,6,10,14
                      .where( [](int a){return a>2 && a<12;}) // 6,10
                      .toVector();

  for (auto i : dst)
    std::cout << i << std::endl;

  return 0;
}
