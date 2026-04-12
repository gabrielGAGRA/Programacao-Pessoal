#include <iostream>
#include <vector>
#include <chrono>
#include <omp.h>
#include <cmath>

using namespace std;

void prime(int num)
{
    int limit = sqrt(num);
    vector<bool> baseSieve(limit + 1, true);
    baseSieve[0] = baseSieve[1] = false;

    // Sequential sieve for base primes
    for (int i = 2; i * i <= limit; i++)
    {
        if (baseSieve[i])
        {
            for (int j = i * i; j <= limit; j += i)
                baseSieve[j] = false;
        }
    }

    vector<int> basePrimes;
    for (int i = 2; i <= limit; i++)
    {
        if (baseSieve[i])
            basePrimes.push_back(i);
    }

    // Parallel segmented sieve
    const int segmentSize = 1000000;
    vector<bool> pno(num + 1, true);
    pno[0] = pno[1] = false;

#pragma omp parallel for schedule(dynamic)
    for (int segStart = 0; segStart <= num; segStart += segmentSize)
    {
        int segEnd = min(segStart + segmentSize - 1, num);

        for (int prime : basePrimes)
        {
            int start = max(prime * prime, (segStart + prime - 1) / prime * prime);
            for (int j = start; j <= segEnd; j += prime)
            {
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