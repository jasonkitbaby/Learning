package com.lock;

import java.util.concurrent.locks.ReentrantReadWriteLock;

/************************************************************
 * Copy Right Information : 
 * Project : ${ProjectName}
 * JDK version used : ${SDK}
 * Comments : 
 *
 * Modification history : 
 *
 * Sr Date Modified By  Comment
 * 1. 2017/2/20 marco Initial

 ***********************************************************/
public class ReentrantReadWriteLockDemo  implements Runnable{

    public static ReentrantReadWriteLock myLock = new ReentrantReadWriteLock();


    @Override
    public void run() {
        myLock.writeLock().lock();
        System.out.println(Thread.currentThread() + "获得写锁");
        myLock.readLock().lock();
        System.out.println(Thread.currentThread() + "获得读锁");
        myLock.readLock().unlock();

        myLock.writeLock().unlock();


    }

    public static void main(String[] arg) throws InterruptedException {

        ReentrantReadWriteLockDemo reentrantReadWriteLockDemo = new ReentrantReadWriteLockDemo();
        Thread t1 = new Thread(reentrantReadWriteLockDemo);
        Thread t2 = new Thread(reentrantReadWriteLockDemo);

        t1.start();
        t2.start();
        t1.join();
        t2.join();

    }
}
