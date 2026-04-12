#include <iostream>
#include <vector>
#include <chrono>
#include <omp.h>

using namespace std;

void prime(int num)
{
    vector<bool> pno(num + 1, true);
    pno[0] = pno[1] = false;

// Handle even numbers first (single threaded - very fast)
#pragma omp parallel for
    for (int i = 4; i <= num; i += 2)
        pno[i] = false;

    // Only process odd primes with better scheduling
    for (int i = 3; i * i <= num; i += 2)
    {
        if (pno[i])
        {
            // Only parallelize for larger primes where work is substantial
            if (i > 1000)
            {
#pragma omp parallel for schedule(static, 1000)
                for (int j = i * i; j <= num; j += 2 * i)
                    pno[j] = false;
            }
            else
            {
                // Sequential for small primes
                for (int j = i * i; j <= num; j += 2 * i)
                    pno[j] = false;
            }
        }
    }
}

int main()
{
    int num = 900000000;
    omp_set_num_threads(22);

    auto start = chrono::high_resolution_clock::now();
    prime(num);
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << "Time taken by function: " << duration.count() << " milliseconds" << endl;
    return 0;
}