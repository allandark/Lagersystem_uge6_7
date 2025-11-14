import "swiper/swiper.css"; 
import { useEffect, useState } from "react";


import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, EffectCreative  } from "swiper/modules";


interface RedditPost {
  title: string;
  url: string;
  permalink: string;
  id: string;
  thumbnail: string;
}

export default function DailyReddit() {
  const [posts, setPosts] = useState<RedditPost[]>([]);
  const [loading, setLoading] = useState(true);
  const n_posts: number = 10;
  useEffect(() => {
    const fetchReddit = async () => {
      try {
        const redditUrl = `https://www.reddit.com/r/ProgrammerHumor/top.json?limit=${n_posts}&t=day`;
        console.log(redditUrl)
        // const encodedUrl = encodeURIComponent(redditUrl);
        const response = await fetch(
            `https://cors-anywhere.com/${redditUrl}`
        );
        console.log(response)
        const redditJson = await response.json();
        console.log(redditJson)
        

        const topPosts: RedditPost[] = redditJson.data.children.map((child: any) => ({
          title: child.data.title,
          url: child.data.url,
          permalink: child.data.permalink,
          id: child.data.id,
          thumbnail: child.data.thumbnail.startsWith("http") ? child.data.thumbnail : "",
        }));

        setPosts(topPosts);
      } catch (err) {
        console.error("Failed to fetch Reddit posts:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchReddit();
  }, []);

  if (loading) return <p className="text-center mt-10 text-gray-400">Loading Daily Memes...</p>;
  if (!posts.length) return <p className="text-center mt-10 text-gray-400">No memes found</p>;

  return (
    <div className="flex justify-center mt-10">
      <div className="w-full max-w-4xl">
        <h2 className="text-3xl font-bold text-center mb-6 text-blue-400 drop-shadow-md">
          Daily Meme
        </h2>
        <Swiper
  modules={[Autoplay, EffectCreative]}
  autoplay={{ delay: 4000 }}
  effect="fade"
  loop
  className="rounded-xl overflow-hidden shadow-lg w-full h-[600px] md:h-[700px]"
>
  {posts.map((post) => {
    // Determine the best image
    // const imageUrl =
    //   post.preview?.images?.[0]?.source?.url
    //     ? post.preview.images[0].source.url.replace(/&amp;/g, "&")
    //     : post.url_overridden_by_dest;

    return (
      <SwiperSlide key={post.id}>
          <div className="relative bg-gray-900 w-130 h-200 mx-auto">
        
        <a
          href={`https://reddit.com${post.permalink}`}
          target="_blank"
          rel="noopener noreferrer"
          className="absolute flex justify-center items-center mx-auto w-fit h-fit bg-gray-900"
        >
            <img
              src={post.url}
              alt={post.title}
              className="w-130 object-contain mx-auto my-auto rounded-xl shadow-md"
            />
        </a>
        </div>

      </SwiperSlide>
    );
  })}
</Swiper>




      </div>
    </div>
  );
}
