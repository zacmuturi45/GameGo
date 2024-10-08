import React from 'react'
import { isaac, grateful } from '../../../public/images'
import FollowData from './followData'
import SearchBar from './searchbar'

export default function Following({ following }) {

    return (
        <div className='follower-maindiv'>
            <div className="follower-div">
                <div className='follower-div-div'>
                    {
                        following.map((data, index) => {
                            return <FollowData image={data.node.profilePic} key={index} name={data.node.username} id={data.node.userid} gameCount={data.node.boughtGames.edges.length} wishlistCount={data.node.userWishlistGames.edges.length} index={index} />
                        })
                    }
                </div>
            </div>
        </div>
    )
}
