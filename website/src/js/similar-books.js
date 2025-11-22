/**
 * Similar Books - 30 YA Romance books with similarities to "The Boy Who Knew Me First"
 * Themes: Sports romance, childhood friends to lovers, fake dating, second chance romance
 */

const similarBooks = [
  // Hockey & Sports Romance
  {
    title: "Icebreaker",
    author: "Hannah Grace",
    isbn: "9781668026151",
    amazonLink: "https://www.amazon.com/Icebreaker-Novel-Hannah-Grace/dp/1668026155",
    cover: "icebreaker.jpg",
    description: "A competitive figure skater and hockey team captain are forced to share a rink, sparking an unexpected romance."
  },
  {
    title: "Wildfire",
    author: "Hannah Grace",
    isbn: "9781668026274",
    amazonLink: "https://www.amazon.com/Wildfire-bestselling-author-Icebreaker-Maple-ebook/dp/B0BV8T39DM",
    cover: "wildfire.jpg",
    description: "Two summer camp counselors navigate a no-fraternizing rule after an unforgettable night together."
  },
  {
    title: "The Deal",
    author: "Elle Kennedy",
    isbn: "9781775293934",
    amazonLink: "https://www.amazon.com/Deal-Off-Campus-Elle-Kennedy/dp/1775293939",
    cover: "the-deal.jpg",
    description: "A college hockey star and a music major make a deal that changes everything in this enemies-to-lovers romance."
  },
  {
    title: "Him",
    author: "Sarina Bowen & Elle Kennedy",
    isbn: "9781942444404",
    amazonLink: "https://www.amazon.com/Him-Sarina-Bowen-ebook/dp/B011LSLI9G",
    cover: "him.jpg",
    description: "Childhood best friends reunite at college hockey, rekindling feelings they never forgot."
  },
  {
    title: "Us",
    author: "Sarina Bowen & Elle Kennedy",
    isbn: "9781942444886",
    amazonLink: "https://www.amazon.com/Us-Elle-Kennedy/dp/1942444885",
    cover: "us.jpg",
    description: "The epic continuation of Jamie and Wes's love story as they navigate life after college hockey."
  },
  {
    title: "Good Boy",
    author: "Elle Kennedy & Sarina Bowen",
    isbn: "9781464227349",
    amazonLink: "https://www.amazon.com/Good-Boy-WAGs-Elle-Kennedy/dp/1464227349",
    cover: "good-boy.jpg",
    description: "A fake dating hockey romance where the family screw-up falls for a wounded hockey hero."
  },
  {
    title: "Mile High",
    author: "Liz Tomforde",
    isbn: "9781728296630",
    amazonLink: "https://www.amazon.com/Mile-High-Windy-City-Book/dp/1728296633",
    cover: "mile-high.jpg",
    description: "A flight attendant and a hockey player are forced together on a season-long journey."
  },
  {
    title: "Pucked",
    author: "Helena Hunting",
    isbn: "9781989185056",
    amazonLink: "https://www.amazon.com/Pucked-Helena-Hunting/dp/1989185053",
    cover: "pucked.jpg",
    description: "A hockey romance full of laughs, love, and unforgettable chemistry."
  },
  {
    title: "Binding 13",
    author: "Chloe Walsh",
    isbn: "9781728299942",
    amazonLink: "https://www.amazon.com/Binding-13-Chloe-Walsh/dp/1728299942",
    cover: "binding-13.jpg",
    description: "An all-star rugby player and a shy girl form an unlikely bond at an elite Irish school."
  },

  // Jenny Han - Childhood Friends to Lovers
  {
    title: "The Summer I Turned Pretty",
    author: "Jenny Han",
    isbn: "9781416968290",
    amazonLink: "https://www.amazon.com/Summer-I-Turned-Pretty/dp/1416968296",
    cover: "summer-i-turned-pretty.jpg",
    description: "Belly has always been in love with Conrad, but one summer changes everything between them."
  },
  {
    title: "It's Not Summer Without You",
    author: "Jenny Han",
    isbn: "9781416995562",
    amazonLink: "https://www.amazon.com/Its-Not-Summer-Without-You/dp/141699556X",
    cover: "not-summer-without-you.jpg",
    description: "The summer after everything changed, Belly must choose between two brothers."
  },
  {
    title: "We'll Always Have Summer",
    author: "Jenny Han",
    isbn: "9781416995586",
    amazonLink: "https://www.amazon.com/Well-Always-Have-Summer/dp/1416995587",
    cover: "always-have-summer.jpg",
    description: "The epic conclusion to the Summer trilogy where Belly makes her final choice."
  },
  {
    title: "To All the Boys I've Loved Before",
    author: "Jenny Han",
    isbn: "9781442426719",
    amazonLink: "https://www.amazon.com/All-Boys-Ive-Loved-Before/dp/1442426713",
    cover: "to-all-the-boys.jpg",
    description: "Lara Jean's secret love letters get mailed, turning her life upside down."
  },
  {
    title: "P.S. I Still Love You",
    author: "Jenny Han",
    isbn: "9781442426733",
    amazonLink: "https://www.amazon.com/P-S-I-Still-Love-You/dp/1442426738",
    cover: "ps-i-still-love-you.jpg",
    description: "Lara Jean navigates a new relationship while an old flame returns from her past."
  },
  {
    title: "Always and Forever, Lara Jean",
    author: "Jenny Han",
    isbn: "9781481418430",
    amazonLink: "https://www.amazon.com/Always-Forever-Lara-Jean/dp/1481418432",
    cover: "always-and-forever.jpg",
    description: "Lara Jean faces her future as she prepares for college and her happily ever after."
  },

  // Lynn Painter - Fake Dating & Rom-Coms
  {
    title: "Better Than the Movies",
    author: "Lynn Painter",
    isbn: "9781534467637",
    amazonLink: "https://www.amazon.com/Better-Than-Movies-Lynn-Painter/dp/1534467637",
    cover: "better-than-movies.jpg",
    description: "A rom-com obsessed teen teams up with her annoying neighbor to win over her childhood crush."
  },
  {
    title: "Betting on You",
    author: "Lynn Painter",
    isbn: "9781665921237",
    amazonLink: "https://www.amazon.com/Betting-You-Lynn-Painter/dp/1665921234",
    cover: "betting-on-you.jpg",
    description: "A teen girl unknowingly becomes the center of a bet while working at a waterpark."
  },
  {
    title: "The Do-Over",
    author: "Lynn Painter",
    isbn: "9781665903820",
    amazonLink: "https://www.amazon.com/Do-Over-Lynn-Painter/dp/1665903821",
    cover: "the-do-over.jpg",
    description: "After the worst Valentine's Day ever, she gets to relive it over and over again."
  },

  // Classic YA Contemporary Romance
  {
    title: "The Upside of Falling",
    author: "Alex Light",
    isbn: "9780062918062",
    amazonLink: "https://www.amazon.com/Upside-Falling-Alex-Light/dp/0062918060",
    cover: "upside-of-falling.jpg",
    description: "A fake relationship between a cynic and a football captain turns into something real."
  },
  {
    title: "The Fill-In Boyfriend",
    author: "Kasie West",
    isbn: "9780062336385",
    amazonLink: "https://www.amazon.com/Fill-Boyfriend-Kasie-West/dp/0062336382",
    cover: "fill-in-boyfriend.jpg",
    description: "After getting dumped at prom, she recruits a stranger to be her fake boyfriend for the night."
  },
  {
    title: "By Your Side",
    author: "Kasie West",
    isbn: "9780062455864",
    amazonLink: "https://www.amazon.com/Your-Side-Kasie-West/dp/0062455869",
    cover: "by-your-side.jpg",
    description: "Accidentally locked in a library for the weekend with the school's notorious troublemaker."
  },
  {
    title: "The DUFF",
    author: "Kody Keplinger",
    isbn: "9780316084239",
    amazonLink: "https://www.amazon.com/DUFF-Kody-Keplinger/dp/0316084239",
    cover: "the-duff.jpg",
    description: "A high school senior and the school's biggest jock form an unexpected enemies-to-lovers connection."
  },
  {
    title: "Tweet Cute",
    author: "Emma Lord",
    isbn: "9781250237323",
    amazonLink: "https://www.amazon.com/Tweet-Cute-Emma-Lord/dp/1250237327",
    cover: "tweet-cute.jpg",
    description: "A viral Twitter war between rival food chains masks a secret online romance."
  },

  // Stephanie Perkins - Paris & Romance
  {
    title: "Anna and the French Kiss",
    author: "Stephanie Perkins",
    isbn: "9780142419403",
    amazonLink: "https://www.amazon.com/Anna-French-Kiss-Stephanie-Perkins/dp/0142419400",
    cover: "anna-french-kiss.jpg",
    description: "A year at a Paris boarding school leads to the most romantic year of Anna's life."
  },
  {
    title: "Lola and the Boy Next Door",
    author: "Stephanie Perkins",
    isbn: "9780142422014",
    amazonLink: "https://www.amazon.com/Lola-Boy-Next-Door-Stephanie/dp/0142422010",
    cover: "lola-boy-next-door.jpg",
    description: "When her childhood crush moves back next door, Lola's carefully crafted world gets complicated."
  },
  {
    title: "Isla and the Happily Ever After",
    author: "Stephanie Perkins",
    isbn: "9780525425632",
    amazonLink: "https://www.amazon.com/Isla-Happily-Ever-After/dp/0525425632",
    cover: "isla-happily.jpg",
    description: "A hopeless romantic finally gets her chance with the gorgeous boy she's been admiring from afar."
  },

  // Morgan Matson - Summer Adventures
  {
    title: "Since You've Been Gone",
    author: "Morgan Matson",
    isbn: "9781442435018",
    amazonLink: "https://www.amazon.com/Since-Youve-Been-Morgan-Matson/dp/1442435011",
    cover: "since-youve-been-gone.jpg",
    description: "A shy teen follows a mysterious to-do list left by her missing best friend."
  },
  {
    title: "Amy & Roger's Epic Detour",
    author: "Morgan Matson",
    isbn: "9781416990659",
    amazonLink: "https://www.amazon.com/Amy-Rogers-Epic-Detour/dp/1416990658",
    cover: "amy-rogers-detour.jpg",
    description: "A cross-country road trip becomes a journey of healing, adventure, and unexpected romance."
  },

  // Rainbow Rowell & Adult Crossover
  {
    title: "Eleanor & Park",
    author: "Rainbow Rowell",
    isbn: "9781250012579",
    amazonLink: "https://www.amazon.com/Eleanor-Park-Rainbow-Rowell/dp/1250012570",
    cover: "eleanor-park.jpg",
    description: "Two misfits fall in love over music and comic books on a school bus in 1986."
  },
  {
    title: "Fangirl",
    author: "Rainbow Rowell",
    isbn: "9781250030955",
    amazonLink: "https://www.amazon.com/Fangirl-Rainbow-Rowell/dp/1250030951",
    cover: "fangirl.jpg",
    description: "A college freshman navigates adulthood while writing fan fiction and finding unexpected love."
  }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = similarBooks;
}
