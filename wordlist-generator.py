import itertools
RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"  
banner = f"""
   {BLUE} 

████████ ██   ██ ███████ ██    ██  █████  ███    ██ 
   ██    ██   ██ ██       ██  ██  ██   ██ ████   ██ 
   ██    ███████ █████     ████   ███████ ██ ██  ██ 
   ██    ██   ██ ██         ██    ██ {RED}J{END}{BLUE} ██ ██  ██ ██ 
   ██    ██   ██ ███████    ██    ██ {RED}A{END}{BLUE} ██ ██   ████ 
                                                    
 {END} 
   """ 
print(banner)
words = input(f"{GREEN} Enter your words/numbers/symbols (space-separated): ").split()
output_file = input(" Output file name (default: wordlist.txt): ").strip() or "wordlist.txt"
limit = int(input("Maximum number of generated words (e.g. 1000000): "))
separators = ['', '.', '_', '-', '@']

# --- Wordlist generation ---
wordlist = set()
print(f"\n {YELLOW} Generating combinations starting ... {END}")

for r in range(2, len(words) + 1):  # Start from combinations of 2 elements
    for combo in itertools.permutations(words, r):
        for sep in separators:
            word = sep.join(combo)
            wordlist.add(word)
            if len(wordlist) >= limit:
                print(f"\n {RED} Limit reached: {limit} words generated.{END}")
                break
        if len(wordlist) >= limit:
            break
    if len(wordlist) >= limit:
        break

with open(output_file, "w", encoding="utf-8") as f:
    for word in sorted(wordlist):
        f.write(word + "\n")

print(f"\n {BLUE} Done! {len(wordlist)} words saved in: {output_file}{END}") 
