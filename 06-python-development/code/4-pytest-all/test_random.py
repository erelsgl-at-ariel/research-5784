"""
איזה בדיקות אפשר להוסיף ב-unittest / pytest
מעבר לבדיקות שב-doctest?

אפשרות אחת היא להוסיף בדיקות על קלטים גדולים שאתם מייצרים באקראי.
איך אפשר לבדוק על קלטים אקראיים אם לא יודעים את התשובה הנכונה? כמה אפשרויות:

א. ייתכן שכבר יש מימוש לאלגוריתם אחר הפותר את אותה בעיה. לדוגמה, בספריה prtpy
יש כמה אלגוריתמים לחישוב חלוקה מאוזנת של מספרים. אם כותבים אלגוריתם חדש לאותה בעיה (יעיל יותר מהקיימים),
אז אפשר להריץ אותו על קלט אקראי, להריץ אלגוריתם קיים על אותו קלט, ולוודא שהתשובה זהה.
הנה דוגמה: https://github.com/erelsgl/prtpy/blob/main/tests/test_complete_greedy.py

ב. אפשרות שניה היא לבדוק תכונות של הפלט, שאנחנו יודעים שצריכות להתקיים בכל מקרה. לדוגמה:
אם מימשתם אלגוריתם לחלוקה הוגנת - אתם יכולים לבדוק שהתוצאה מקיימת את תכונות ההוגנות הדרושות.
אם מימשתם אלגוריתם למציאת שידוך בגרף - אתם יכולים לבדוק שהתוצאה מקיימת את ההגדרה של שידוך.
וכו'.

ג. גם אם אף אחת מהאפשרויות הקודמות לא עובדת, עדיין כדאי להריץ את האלגוריתם על קלט גדול אקראי, ולבדוק שהוא לפחות מחזיר תוצאה כלשהי, ולא קורס או נתקע.

"""