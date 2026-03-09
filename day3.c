//cs50 如何来实现一个线性搜索
#include<stdio.h>
#include<cs50.h>

int main(void){
    int nums[] = {100,60,5,2,30,1,18};
    int n = get_int("Number: ");
    for(int i = 0; i < 7;i++){
        if(nums[i] == n){
            printf("Found\n");
            return 0;//结束 ，不然会打印not found
        }
           
    } //模拟第一个志愿者从左到右一个一个搜索储物柜，查看里面的数字
    printf("Not found\n");
    return 1;
}

//要是数组没有初始化呢？ 
//int nums[7];  这七个位置我们根本没放任何数据，但是可能有垃圾值（内存中残留的数据）
//一直试，我敢说肯定能找到实际存在的数字


//如果是比较字符串是否相等呢

#include<string.h>
if(strcmp(s1,s2) == 0)
//不能直接用==比较string

//现在来设计一个查找电话薄
#include<stdio.h>
#include<cs50.h>
#include<string.h>

int main(){
    string names[] = {"bigguy","liyut","lichunt"};
    string nums[] = {"2215189","18945311572","18825664889"};
    string name = get_string("Name: ");
    for(int i = 0;i < 3;i++){
        if(strcmp(names[i],name) == 0){
            printf("Found %s\n",nums[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}