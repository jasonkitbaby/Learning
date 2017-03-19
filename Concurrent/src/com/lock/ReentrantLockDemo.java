package com.lock;


import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantLock;

public class ReentrantLockDemo implements Runnable{


    public static ReentrantLock reEntrantLock = new ReentrantLock();
    public static ReentrantLock fairReEntrantLock = new ReentrantLock(true);
    public static int i = 0;

    @Override
    public void run() {

        // 重入锁
        for(int j = 0; j< 10000; j++){
            try{
                reEntrantLock.lock();
                reEntrantLock.lock();
                i++;
            }finally {
                reEntrantLock.unlock();
                reEntrantLock.unlock();
            }
        }



        try{

            // tryLock
            reEntrantLock.tryLock();   // 无参数 立即返回
            reEntrantLock.tryLock(5,TimeUnit.SECONDS);


            if(reEntrantLock.tryLock(5, TimeUnit.SECONDS)){
                Thread.sleep(5000);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }finally {
            if(reEntrantLock.isHeldByCurrentThread()){
                reEntrantLock.unlock();
            }
        }

    }

    public static void main(String[] arg) throws InterruptedException {

        ReentrantLockDemo  demo = new ReentrantLockDemo();

        Thread t1 = new Thread(demo);
        Thread t2 = new Thread(demo);

        t1.start();t2.start();
        t1.join();t2.join();

        System.out.println(i);
    }
}
