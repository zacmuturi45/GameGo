import Image from 'next/image'
import React from 'react'
import { plusWhite } from '../../../public/images'

export default function GameUsers({ image, name, edits, followerCount }) {
    return (
        <main className='main-game-users'>
            <div className='main-game-users-div1'>
                <div className="image-div">
                    <Image src={image} alt='profile-image' className='profile-image' />
                </div>
                <div className='text-div'>
                    <p>{name}</p>
                    <p>{edits} edits</p>
                </div>
            </div>

            <div className='main-game-users-div2'>
                    <Image src={plusWhite} alt='plusWhite' width={8} height={8} className='span' />
                    <p>Follow</p>
                <p className='followercount'>{followerCount}</p>
            </div>
        </main>
    )
}
