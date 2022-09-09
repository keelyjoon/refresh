#include <stdio.h>
#include <stdlib.h>

struct Point{
    float x;
    float y;
};

typedef struct Point Point;

Point myPoint;
myPoint.x = 4.3;
myPoint.y 7.1;

Point myOtherPoint{3.8, 2.7};