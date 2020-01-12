// backjoon 2869번 문제
// 달팽이는 올라가고 싶다

#include <stdio.h>

int main(){
    // A = 달팽이가 낮에 올라갈 수 있는 길이
    // B = 달팽이가 밤에 떨어지는 길이
    // V = 나무 길이
    // day = 나무에 올라갈 날자
    int A, B, V, day = 0;
    scanf("%d %d %d",&A, &B, &V);
    
    day = (V - B - 1) / (A - B) + 1;
    
    printf("%d\n", day);
    
    return 0;
}
