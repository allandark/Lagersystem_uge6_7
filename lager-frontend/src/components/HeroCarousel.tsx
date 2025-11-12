import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, EffectFade } from "swiper/modules";

import "swiper/css";
import "swiper/css/effect-fade";

const images = [
  "/src/assets/meme1.jpg",
  "/src/assets/meme2.jpg",  
];

export default function HeroCarousel() {
  return (
    <Swiper
      modules={[Autoplay, EffectFade]}
      effect="fade"
      loop
      autoplay={{ delay: 4000, disableOnInteraction: false }}
      className="w-full h-96 md:h-[500px] rounded-xl overflow-hidden shadow-lg bg-gray-900"//
    >
      {images.map((img, i) => (
        <SwiperSlide key={i} className="flex justify-center items-center bg-gray-900">
          <img
            src={img}
            alt={`Slide ${i + 1}`}
            className="max-w-full max-h-full object-contain"
          />
        </SwiperSlide>
      ))}
    </Swiper>
  );
}
