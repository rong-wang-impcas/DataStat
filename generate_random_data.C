{

	int Nnormal = 100;
	int Nabnormal = 2;

	ofstream fout("data.txt");
	for(int i=0;i<Nnormal;i++) fout<<  gRandom->Gaus(2, 1) <<endl;
	for(int i=0;i<Nabnormal;i++) fout<<  10 + gRandom->Gaus(2, 1) <<endl;






}
