package main

import (
	"fmt"
	"time"
)

type Job struct {
	Name   string
	Delay  time.Duration
	Number int
}

type Worker struct {
	Id         int
	JobQueue   chan Job
	WorkerPool chan chan Job
	QuitChan   chan bool
}

type Dispatcher struct {
	WorkerPool chan chan Job
	MaxWorker  int
	JobQueue   chan Job
}

func NewWorker(id int, workerPool chan chan Job) *Worker {
	return &Worker{
		Id:         id,
		JobQueue:   make(chan Job),
		WorkerPool: workerPool,
		QuitChan:   make(chan bool),
	}
}
func (w Worker) Start() {
	go func() {
		for {
			w.WorkerPool <- w.JobQueue
			select {
			case job := <-w.JobQueue:
				fmt.Printf("Worker with id %d started\n", w.Id)
				fib := Finobacci(job.Number)
				time.Sleep(job.Delay)
				fmt.Printf("Worker with id %d finished with result %d", w.Id, fib)
			case <-w.QuitChan:
				fmt.Printf("Worker with id %d stopped\n", w.Id)
			}
		}
	}()
}

func (w Worker) Stop() {
	go func() {
		w.QuitChan <- true
	}()
}

func Finobacci(n int) int {
	if n <= 1 {
		return n
	}
	return Finobacci(n-1) + Finobacci(n-2)
}

func NewDispatcher(jobQueue chan Job, maxWorkers int) *Dispatcher {
	return &Dispatcher{
		JobQueue:   jobQueue,
		MaxWorker:  maxWorkers,
		WorkerPool: make(chan chan Job, maxWorkers),
	}
}

func (d *Dispatcher) Dispatch() {
	for {
		select {
		case job := <-d.JobQueue:
			go func() {
				workerJobQueue := <-d.WorkerPool
				workerJobQueue <- job
			}()
		}
	}
}
