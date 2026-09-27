#ifndef LATENCY_MONITOR_H
#define LATENCY_MONITOR_H

#include <vector>
#include <string>
#include <fstream>

// Function prototypes
int errorBoundFormula(double, double, double);
double bellCurveFunction(double, double, double);
void dataMunch(const std::vector<double>&, double&, double&);
std::vector<double> collectLatencyData(int,std::fstream&, std::string);

#endif