from math import ceil
from datetime import date, datetime, timedelta
from typing import Optional, Union, Dict

import attr


year_mon_day = "%Y-%m-%d"
mon_day_year = "%m-%d-%Y"
day_mon_year = "%d-%m-%Y"


@attr.s
class SMTwo:
    easiness = attr.ib(validator=attr.validators.instance_of(float))
    interval = attr.ib(validator=attr.validators.instance_of(int))
    repetitions = attr.ib(validator=attr.validators.instance_of(int))
    review_date = attr.ib(init=False)

    @staticmethod
    def first_review(
        quality: int,
        review_date: Optional[Union[date, str]] = None,
    ) -> "SMTwo":
        if not review_date:
            review_date = date.today()

        return SMTwo(2.5, 0, 0).review(quality, review_date)

    def review(
        self,
        quality: int,
        review_date: Optional[Union[date, str]] = None,
    ) -> "SMTwo":
        if not review_date:
            review_date = date.today()

        if isinstance(review_date, str):
            review_date = datetime.strptime(review_date, year_mon_day).date()

        if quality < 3:
            self.interval = 1
            self.repetitions = 0
        else:
            if self.repetitions == 0:
                self.interval = 1
            elif self.repetitions == 1:
                self.interval = 6
            else:
                self.interval = ceil(self.interval * self.easiness)

            self.repetitions = self.repetitions + 1

        self.easiness += 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
        self.easiness = max(self.easiness, 1.3)
        review_date += timedelta(days=self.interval)
        self.review_date = review_date

        return self


# review = sm2.review(quality=5)
# review = SMTwo.first_review(quality=5, review_date="2023-09-03")
# print(review)
# rv = SMTwo(review.easiness, review.interval, review.repetitions).review(2, "2023-09-03")
# print(rv)
