package com.word;

import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

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
public class WordCountReducer extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {

    @Override
    public void reduce(Text key, Iterator<IntWritable> values,
                       OutputCollector<Text, IntWritable> output, Reporter reporter)
            throws IOException {
        int count = 0;
        while(values.hasNext()) {
            values.next();
            count++;
        }
        output.collect(key, new IntWritable(count));
    }

}
