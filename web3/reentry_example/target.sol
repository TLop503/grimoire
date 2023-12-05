// taken verbatim from Zane's code

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IDailyClient {
    function processDaily(uint256 newPoints) external;
}

contract Pointless {
    mapping(address => uint256) points;
    mapping(address => uint) claims;

    event StreakReward(bytes32 token);

    function claimDaily() public {
        // Ensure daily reward is claimed at most once per 24-hour period
        require(block.timestamp >= claims[msg.sender] + 1 days);

        // Give user points
        points[msg.sender] += 10;

        // Allow sender to process daily claim
        IDailyClient(msg.sender).processDaily(points[msg.sender]);

        // Update claim time to prevent several claims within a day
        claims[msg.sender] = block.timestamp;
    }

    function claimStreakReward(bytes32 token) public {
        require(points[msg.sender] >= 100);

        emit StreakReward(token);
    }
}
