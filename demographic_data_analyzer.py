
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(
        "adult.data.csv",
        skipinitialspace=True
    )

    # Convert numeric columns to numbers
    df["age"] = pd.to_numeric(df["age"])
    df["hours-per-week"] = pd.to_numeric(df["hours-per-week"])

    # 1. How many people of each race?
    race_count = df["race"].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(),
        1
    )

    # 3. What percentage of people have a Bachelor's degree?
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # 4. What percentage of people with advanced education make >50K?
    # Advanced education = Bachelors, Masters, Doctorate
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (
            df.loc[higher_education, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # 5. What percentage of people without advanced education make >50K?
    lower_education_rich = round(
        (
            df.loc[~higher_education, "salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # 7. What percentage of people who work the minimum hours
    # have a salary of >50K?
    num_min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (
            num_min_workers["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # 8. What country has the highest percentage of people
    # that earn >50K?
    country_salary_percentage = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_salary_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_salary_percentage.max(),
        1
    )

    # 9. Identify the most popular occupation for those
    # who earn >50K in India.
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = (
        india_rich["occupation"]
        .value_counts()
        .idxmax()
    )

    # Print results
    if print_data:
        print("Number of each race:")
        print(race_count)

        print("Average age of men:", average_age_men)

        print(
            "% of people with Bachelors degrees:",
            percentage_bachelors
        )

        print(
            "% of people with higher education that earn >50K:",
            higher_education_rich
        )

        print(
            "% of people without higher education that earn >50K:",
            lower_education_rich
        )

        print(
            "Min work time:",
            min_work_hours,
            "hours/week"
        )

        print(
            "% of people who work minimum hours and earn >50K:",
            rich_percentage
        )

        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )

        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )

        print(
            "Top occupations in India:",
            top_IN_occupation
        )

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
