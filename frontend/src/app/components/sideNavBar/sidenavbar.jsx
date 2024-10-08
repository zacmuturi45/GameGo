"use client"

import React, { useEffect, useRef, useState } from 'react'
import "../../css/index.css"
import Link from 'next/link'
import Image from 'next/image';
import { newReleases, genres, platforms, arrowDown, isLoggedIn, gradients, getMiddleDigit } from '../../../../public/images';
import SideNavBox from '../sideNavBox';
import gsap from 'gsap';
import ScrollTrigger from 'gsap/src/ScrollTrigger';
import { useFilter } from '@/app/contexts/sidenavContext';
import { useLoggedUser } from '@/app/contexts/loginContext';
import NameCircle from '../nameCircle';
import { useRouter } from 'next/navigation';

export default function SideNavBar({ main }) {

  gsap.registerPlugin(ScrollTrigger);
  const [toSlice, setToSlice] = useState(3);
  const [toSlice1, setToSlice1] = useState(3);
  const { setFilter, filter } = useFilter();
  const [visible, setVisible] = useState(true);
  const [visible1, setVisible1] = useState(true);
  const router = useRouter();
  const sidenavRef = useRef(null);
  const { userInfo } = useLoggedUser();

  const handlePlatforms = () => {
    setToSlice(platforms.length)
    setVisible(false)
  }

  const handlePlatforms1 = () => {
    setToSlice1(genres.length)
    setVisible1(false)
  }


  return (
    <div className='sidenavbar dsp-f fd-c col-12-xs' ref={sidenavRef}>
      <div className='sidenavbar-content'>
        <Link href="/" className='links linksh2'><h2 onClick={() => setFilter("Home")}>Home</h2></Link>
      </div>

      {userInfo.username && <div className='sidenav-profile-name' onClick={() => router.push(`/users/${userInfo.userid}`)}>{userInfo.username.length >= 10 ? (<span style={{marginRight: 15, textTransform: "capitalize", fontSize: "1.2rem", fontWeight: 700, letterSpacing: 1}}>{userInfo.username.slice(0, 10)}...</span>) : (<span style={{marginRight: 10, textTransform: "capitalize", fontSize: "1.2rem", fontWeight: 700, letterSpacing: 1}}>{userInfo.username}</span>)}<NameCircle name={userInfo.username.slice(0, 1)} gradient={gradients[getMiddleDigit(userInfo.userid)]} /></div>}

      <div className='sidenavbar-children'>
        <div className='box'>
          <h2>New Releases</h2>
          {
            newReleases.map((item, index) => (
              <div key={index} className='sidenavbox-container'>
                <SideNavBox image={item.image} text={item.text} />
              </div>
            ))
          }
        </div>

        <div className='mt-3 box'>
          <h2>Browse</h2>
          <h2>Platforms</h2>
          {
            platforms.slice(0, toSlice).map((item, index) => (
              <div key={index} className='sidenavbox-container'>
                <SideNavBox image={item.image} text={item.text} />
              </div>
            ))
          }
          <div className='sidenavbox mt-1' onClick={() => handlePlatforms()}>
            <Image src={arrowDown} alt="svg-image" width={30} height={30} className={visible ? "visible" : "invisible"} />
            <p style={{ color: "lightgray" }} className={visible ? "visible" : "invisible"}>Show all</p>
          </div>

          <div
            className='sidenavbox mt-1'
            onClick={() => {
              setToSlice(3)
              setVisible(true)
            }}
          >
            <Image src={arrowDown} alt="svg-image" width={30} height={30} className={visible ? "invisible img" : "visible img"} />
            <p style={{ color: "lightgray" }} className={visible ? "invisible" : "visible"}>Hide</p>
          </div>
        </div>

        <div className='mt-3 box'>
          <h2>Genres</h2>
          {
            genres.slice(0, toSlice1).map((item, index) => (
              <div key={index} className='sidenavbox-container'>
                <SideNavBox image={item.image} text={item.text} />
              </div>
            ))
          }
          <div
            className='sidenavbox mt-1'
            onClick={() => handlePlatforms1()}
          >
            <Image src={arrowDown} alt="svg-image" width={30} height={30} className={visible1 ? "visible" : "invisible"} />
            <p style={{ color: "lightgray" }} className={visible1 ? "visible" : "invisible"}>Show all</p>
          </div>

          <div
            className='sidenavbox mt-1'
            onClick={() => {
              setToSlice1(3)
              setVisible1(true)
            }}
          >
            <Image src={arrowDown} alt="svg-image" width={30} height={30} className={visible1 ? "invisible img" : "visible img"} />
            <p style={{ color: "lightgray" }} className={visible1 ? "invisible" : "visible"}>Hide</p>
          </div>
        </div>
      </div>
    </div>
  )
}
