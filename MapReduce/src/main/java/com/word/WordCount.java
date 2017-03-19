package com.word;

import org.apache.hadoop.mapred.JobConf;

import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;



/************************************************************
 * Copy Right Information :
 * Project : ${ProjectName}
 * JDK version used : ${SDK}
 * Comments :
 *
 * Modification history :
 *
 * Sr Date       Modified By     Why & What is modified
 * 1. 2017/1/5   marco           Initial

 ***********************************************************/
public class WordCount {

    public static void main(String[] args) throws IOException {
        if(args.length != 2) {
            System.err.println("Error!");
            System.exit(1);
        }

        JobConf conf = new JobConf(WordCount.class);
        conf.setJobName("word count mapreduce demo");

        conf.setMapperClass(WordCountMapper.class);
        conf.setReducerClass(WordCountReducer.class);
        conf.setOutputKeyClass(Text.class);
        conf.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));

        JobClient.runJob(conf);

    }
}
