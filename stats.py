import parser
from collections import defaultdict


def get_percentage(obtained, out_of, round_off=3):
    return round(obtained / out_of * 100, round_off)


def sop(word, n):
    # returns the word depending upon the number of elements we have.
    # for example: sop('tag', 100) => 'tags'
    #            : sop('tag', 1) => 'tag'
    return word + ('', 's')[n > 1]


if __name__ == '__main__':
    dataset_file_name = 'hindi.pos'
    one_dict = defaultdict(set)   # This will store word:set(tags)

    # getting tags of sentences stored in dataset
    tagged_words = parser.POSParser().parse_file(dataset_file_name)

    # tagged_words is list of list of Tag objects, flattening it into list(Tag).
    flattened = sum(tagged_words, [])

    # finding all the possible tags for a given word.
    for tag in flattened:
        one_dict[tag.data].add(tag.tag)

    # counting the number of words having how n tags.
    count_tags = defaultdict(int)
    for word, set_tags in one_dict.items():
        count_tags[len(set_tags)] += 1

    for _len, n_words in count_tags.items():
        print("{} {} in the Dataset {} {} {}".format(n_words, sop('word', n_words), ('has', 'have')[n_words > 1], _len, sop('tag', _len)))

    total_n_tags = sum(count_tags.values())
    n_ambiguous_tags = count_tags.get(1, 0)
    n_unambiguous_tags = total_n_tags - n_ambiguous_tags
    per_ambi = get_percentage(n_ambiguous_tags, total_n_tags)
    per_unambi = get_percentage(n_unambiguous_tags, total_n_tags)

    print("Total Number of tags:", total_n_tags)
    print("Number of Ambiguous tags: {} ({}%)".format(n_ambiguous_tags, per_ambi))
    print("Number of UnAmbiguous tags: {} ({}%)".format(n_unambiguous_tags, per_unambi))

