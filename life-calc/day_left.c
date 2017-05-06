#include <stdio.h>
#include <time.h>
#ifdef __APPLE__
#include <sys/malloc.h>
#else
#include <malloc.h>
#endif
#include <stdlib.h>

#define END_OF_AGE 80

struct Cal_t {
	int cur_year;
    int day_cnt;
    int week_cnt;
    int month_cnt;
};

int leap_year[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int normal_year[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

struct Cal_t *calendar;

int add_days(int month_day[], struct tm *p)
{
    int sum_days = 0, idx;
    for (idx = 0; idx < p->tm_mon; idx += 1) {
        sum_days += month_day[idx];
	}
	sum_days += p->tm_mday;

    return sum_days;
}

void genCalendar(struct tm *p)
{
    // generate Calendar for 100 years from current year
    int idx = 0;
    
    calendar = malloc(sizeof(struct Cal_t)*100);

    if (NULL == calendar) {
        printf ("No enough mem for Calendar\n");
        exit(-1);
    }

    for (idx = 0; idx < 100; idx += 1) {
        int year = 1900 + p->tm_year+idx;
		calendar[idx].cur_year = year;
        if (0 == idx) {
			printf("month = %d, day = %d\n", p->tm_mon, p->tm_mday);
            calendar[idx].month_cnt = 12-p->tm_mon;
            if (0 == year%4)
                calendar[idx].day_cnt = 366-add_days(leap_year, p);
            else
                calendar[idx].day_cnt = 365-add_days(normal_year, p);
            calendar[idx].month_cnt = 12-(1+p->tm_mon);
        }
        else {
            if (0 == year%4) {
                calendar[idx].day_cnt = 366;
            }
            else
                calendar[idx].day_cnt = 365;
            calendar[idx].month_cnt = 12;
        }

        calendar[idx].week_cnt = calendar[idx].day_cnt/7;
    }
}

int calculateDay(int age)
{
    int year_cnt = END_OF_AGE - age;
    int sum_days = 0, idx;

    for (idx = 0; idx < year_cnt; idx += 1)
        sum_days += calendar[idx].day_cnt;

    return sum_days;
}

void show_detail(int age)
{
	int idx;

	for (idx = age; idx < END_OF_AGE; idx += 1) {
		printf("Year/Age:\tmonths\tweeks\tdays\n");
		printf("%d/%d:\t%d\t%d\t%d\n", calendar[idx-age].cur_year, idx, calendar[idx-age].month_cnt, calendar[idx-age].week_cnt, calendar[idx-age].day_cnt);
	}
}

void clear()
{
    if (calendar)
        free(calendar);
}

int main(int argc, char *argv[])
{
	/*
	 * Calculate your day left in this world
	 */
	int age, dayleft;
	time_t timep;
	struct tm *p;
	printf("Enter Your Age: ");
	scanf("%d", &age);

	//printf("Your age = %d.\n", age);
	time(&timep);
	p = gmtime(&timep);
	//printf("%d:%d:%d\n", 1900+p->tm_year, 1+p->tm_mon, p->tm_mday);
	//year = 1900+p->tm_year;
	//month = 1+p->tm_mon;
	//day = p->tm_mday;
    genCalendar(p);

	dayleft = calculateDay(age);
    printf ("Your Days Left = %d\n", dayleft);
	show_detail(age);

    clear();

	return 0;
}
