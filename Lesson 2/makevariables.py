Jame = "12th January 2014"
Olivia = "17th July 2015"
Jake = "11th December 2019"
Amy = "1st February"
Charles = "15th September 2018"

# Version 1
print("James was born in ", Jame, ". Olivia was born in ", Olivia, ". Jake ws born in ", Jake, ". Amy was born in ", Amy, "Charles was born in ", Charles)

# Version 2
print(f"James was born in {Jame}. Olivia was born in {Olivia}. Jake was born in {Jake}. Amy was born in {Amy}. Charles was born in {Charles}.")

# Version 3
print("James was born in {}. Olivia was born in {}. Jake was born in {}. Amy was born in {}. Charles was born in {}".format(Jame, Olivia, Jake, Amy, Charles))

# Version 4
print("James was born in {4}. Olivia was born in {0}. Jake was born in {1}. Amy was born in {2}. Charles was born in {3}".format(Olivia, Jake, Amy, Charles, Jame))