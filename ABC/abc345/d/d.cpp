#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N, H, W;
vector<pair<int, int>> tills;

int solve(int unused, vector<vector<int>> board, int prev_y)
{
    int is_full = 1;
    for (int i = prev_y; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            if (board[i][j] == 0)
            {
                is_full = 0;
                break;
            }
        }
        if (!is_full)
            break;
        prev_y = i + 1;
    }
    if (is_full)
    {
        return 1;
    }
    for (int n = 0; n < N; n++)
    {
        if (unused & (1 << n))
        {
            int A = tills[n].first;
            int B = tills[n].second;
            for (int y = prev_y; y < H - A + 1; y++)
            {
                for (int x = 0; x < W - B + 1; x++)
                {
                    if (board[y][x] > 0)
                        continue;
                    int can = 1;
                    for (int dy = 0; dy < A; dy++)
                    {
                        for (int dx = 0; dx < B; dx++)
                        {
                            if (board[y + dy][x + dx] > 0)
                            {
                                can = 0;
                                break;
                            }
                        }
                    }
                    if (can)
                    {
                        for (int dy = 0; dy < A; dy++)
                        {
                            for (int dx = 0; dx < B; dx++)
                            {
                                board[y + dy][x + dx] = 1;
                            }
                        }
                        if (solve(unused ^ (1 << n), board, prev_y))
                        {
                            return 1;
                        }
                        for (int dy = 0; dy < A; dy++)
                        {
                            for (int dx = 0; dx < B; dx++)
                            {
                                board[y + dy][x + dx] = 0;
                            }
                        }
                    }
                }
            }
            if (A != B)
            {
                for (int y = prev_y; y < H - B + 1; y++)
                {
                    for (int x = 0; x < W - A + 1; x++)
                    {
                        if (board[y][x] > 0)
                            continue;
                        int can = 1;
                        for (int dy = 0; dy < B; dy++)
                        {
                            for (int dx = 0; dx < A; dx++)
                            {
                                if (board[y + dy][x + dx] > 0)
                                {
                                    can = 0;
                                    break;
                                }
                            }
                        }
                        if (can)
                        {
                            for (int dy = 0; dy < B; dy++)
                            {
                                for (int dx = 0; dx < A; dx++)
                                {
                                    board[y + dy][x + dx] = 1;
                                }
                            }
                            if (solve(unused ^ (1 << n), board, prev_y))
                            {
                                return 1;
                            }
                            for (int dy = 0; dy < B; dy++)
                            {
                                for (int dx = 0; dx < A; dx++)
                                {
                                    board[y + dy][x + dx] = 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return 0;
}
int main()
{
    cin >> N >> H >> W;
    for (int i = 0; i < N; i++)
    {
        int A, B;
        cin >> A >> B;
        tills.push_back({A, B});
    }
    vector<vector<int>> board(H, vector<int>(W, 0));
    if (solve((1 << N) - 1, board, 0))
    {
        cout << "Yes\n";
    }
    else
    {
        cout << "No\n";
    }
    return 0;
}