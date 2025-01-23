def main():
    
    input_filename = input().strip()

    tv_shows = {}

    with open(input_filename, 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):    
        num_seasons = int(lines[i].strip())
        tv_show = lines[i + 1].strip()

        if num_seasons not in tv_shows:
            tv_shows[num_seasons] = [tv_show]
        else:
            tv_shows[num_seasons].append(tv_show)
    with open('output_keys.txt', 'w') as file:
        for seasons in sorted(tv_shows.keys()):
            shows = '; '.join(tv_shows[seasons])
            file.write(f"{seasons}: {shows}\n")  
    with open('output_titles.txt', 'w') as file:
        # Create a sorted list of all TV shows
        all_shows = []
        for shows in tv_shows.values():
            all_shows.extend(shows) 
        for show in sorted(all_shows):
            file.write(f"{show}\n")
if __name__ == "__main__":
    main()
