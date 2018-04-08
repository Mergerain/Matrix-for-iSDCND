//
//  Matrices Product.cpp
//  Matrices Product
//
//  Created by Wei Xiong on 4/7/18.
//  Copyright © 2018 Wei Xiong. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;
vector < vector<float> > matrixproduct (vector< vector<float> >mone, vector< vector<float> > mtwo);
int main(){
    vector < vector<float > > mone (3,vector<float>(4,1));
    vector < vector<float > > mtwo (4,vector<float>(3,1));
    
    vector<vector<float>> mproduct (matrixproduct(mone,mtwo));
    cout<<mproduct.size();
    for (int i=0; i< mproduct.size();i++){
        for(int j=0; j<mproduct[0].size();j++){
            cout<<mproduct[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}

vector < vector<float> > matrixproduct (vector< vector<float> >mone, vector< vector<float> > mtwo)
{
    vector < vector <float> > mpro(mone.size());
    if (mone[0].size() != mtwo.size()){
        cout << "Invaild product due to inequal of mone column and mtwo row!";
    }
    else
    {
        vector<vector<float>> mpro (mone.size());
        for (int i=0; i<mone.size();i++)
        {
            for (int j=0; j<mtwo[0].size();j++)
            {
                float sum =0;
                for (int z=0; z<mone[0].size();z++)
                {
                   sum =sum + mone[i][z] * mtwo[z][i];
                }
                mpro[i].push_back(sum);
            }
        }
    }
    return mpro;
}
