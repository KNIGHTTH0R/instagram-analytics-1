from collections import defaultdict

hashtags_dictionary = defaultdict(list)

engagement_dictionary = defaultdict(int)

if input("View or change: ") == "change":
    while 1 == 1:
        if input("Ready (y/n): ") == "y":
            likes = int(input("Likes: "))
            followers = int(input("Followers: "))
            hashtags = input("Hashtags: ").split(" ")
            ratio = likes/followers
            for hashtag in hashtags:
                hashtags_dictionary[hashtag].append(ratio)
            print(hashtags_dictionary)
        else:
            break

for hashtag in hashtags_dictionary:
    hashtags_count = len(hashtags_dictionary[hashtag])
    #print(hashtags_count)
    hashtags_sum = sum(hashtags_dictionary[hashtag])
    #print(hashtags_sum)
    hashtags_engagement = hashtags_sum/hashtags_count
    #print(hashtags_engagement)
    engagement_dictionary[hashtag] = hashtags_engagement
    
print(engagement_dictionary)


           






