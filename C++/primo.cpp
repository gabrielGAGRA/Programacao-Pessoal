#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

void prime(int num)
{
    vector<bool> pno(num + 1, true);
    pno[0] = pno[1] = false;

    for (int i = 2; i * i <= num; i++)
    {
        if (pno[i])
        {
            for (int j = i * i; j <= num; j += i)
                pno[j] = false;
        }
    }

    // Collect primes into a single string for faster output
    string primes;
    for (int i = 2; i <= num; i++)
    {
        if (pno[i])
            primes += to_string(i) + " ";
    }
    // cout << primes << endl;
}

int main()
{
    int num = 900000000;
    // cout << "The prime numbers up to " << num << " are: ";
    auto start = chrono::high_resolution_clock::now();
    prime(num);
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << "Time taken by function: " << duration.count() << " milliseconds" << endl;
    return 0;
}