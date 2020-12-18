/*
 * while.cpp
 *
 * Copyright 2020 olaf5 <olaf5@DESKTOP-T1JQ8NP>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    float a,b;

    for(;true;) {
        cin >> a >> b;
        if (b!=0) cout << a/b << endl;
        else break;

    }

/*
    do
    {
        cin >> a >> b;
        if (b !=0) cout << a/b << endl;
    }
    while (b!=0);
/*
    while (b != 0)
    {
        cin >> a;
        cin >> b;
        if (b!=0)
        cout << a/b << endl;
    }
/*
    {
    while (true)
    {
        cin >> a;
        cin >> b;
        if (b==0) break;
        cout << a/b << endl;
    }

*/
    return 0;
}
