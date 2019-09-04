using System;
using Robocode;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AMF
{
    class MyRobot : Robot
    {
        public override void Run()
        {
            TurnLeft(Heading - 90);

            TurnGunRight(90);

            while (true)
            {
                Ahead(100);
                TurnRadarLeft(180);
                TurnRight(360);

                Back(100);
                TurnRadarRight(180);
                TurnGunLeft(360);
            }
        }

        public override void OnScannedRobot(ScannedRobotEvent e)
        {
            Fire(1);
            FireBullet(3);





        }
    }
}