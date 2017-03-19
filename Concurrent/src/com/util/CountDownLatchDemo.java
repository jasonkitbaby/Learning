package com.util;


import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class CountDownLatchDemo implements Runnable{

    static final java.util.concurrent.CountDownLatch end = new java.util.concurrent.CountDownLatch(10);


    @Override
    public void run() {

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("check complete");
        System.out.println(end.getCount());
        end.countDown();
    }



    public static void main(String[] arg){
        ExecutorService executorService = Executors.newFixedThreadPool(10);

        for(int i =0;i<=9;i++){
            executorService.submit(new CountDownLatchDemo());
        }

        try {
            end.await();
            System.out.println("go");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }
}
