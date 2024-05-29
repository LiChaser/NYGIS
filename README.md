## 关于体育理论测试的满分技巧

最近突发奇想，计划开始写一些GitHub项目，写一个受众广泛又容易被大家接受的小trick，希望可以帮助到你。讲一下我的基本思路:因为学期期末将至，每个学期的体育理论也开始开放，面对平常从不接触的理论知识大家都有所头疼，我就想能否写一个搜题脚本来提高正确率，开始的常规思路是拿取到传输的题目数据，然后进行处理进行调用自动化api来输出答案传参。在摸索的过程中我发现给小bug从而简化了本次操作流程，因为此考试的次数是无限次且会回显分数，所以我可以调整每个题目的答案来遍历实现爆破实验。

在开始之前屏幕前的你需要准备两样工具。

https://www.ddosi.org/burpsuite-pro-bcheck/ 按照教程完成burp的安装

https://pan.baidu.com/s/1Kf5IVDAgVmCgsXU9rRlJXw?login_type=weixin&pwd=fsuj&_at_=1716446871238  proxifier的安装

https://blog.csdn.net/CKT_GOD/article/details/134076065 完整合体运用教程

安装好后确保burp处在打开状态

![image-20240529191446921](https://github.com/1nyg/NYG/blob/main/image-20240529191354671.png)

进入体育公众号点击理论考试

![image-20240529191354671](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240529191354671.png)

我们发现burp亮起抓到了数据，这里最为重要的就是userinfos的参数，就是你账号的认证信息，仔细看参数到&(包括&）后面的数据是不要的，需要自己识别。

![image-20240529191908383](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240529191908383.png)

拿到cookie后运行脚本1，可以看到分数通过暴力可以增长(其实可以通过算法加快速度很多)，这里默认是98分，第一个参数由于格式问题为了方便没调，prev就是第一个参数,这里默认第一个不参与验证爆破，如果需要满分,通过调整这里的prev_data参数看第一个输出得分是否能达到4即可。

![image-20240529193420824](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240529193420824.png)

运行完后可以通过脚本2来查询成绩

![image-20240529193733712](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240529193733712.png)

打开自己的公众号查看发现成功

![image-20240529193858546](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20240529193858546.png)

本次测试就到这就结束了，0基础的同学只需要实现抓包拿取自己的cookie就可以了，剩下就运行脚本即可。整体复杂度不高，但复现的过程很有意思大家可以仔细领略,需要的同学可以自取顺便收藏start，以后会陆续发布关于一些基础的脚本(体育跑步🏃‍，视频倍速刷取~)
